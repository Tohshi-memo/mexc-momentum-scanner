# Decision Report

- generated_at: 2026-05-07T16:22:51.799648+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3657, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.35% | **+0.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.18% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.19% | **+1.64%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 21件 (TP 6 / SL 13 / EXP 2)
- 最新: FHE/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 151件 (Win 46 / Loss 53 / Flat 52) / skip 67件
- 成長率目線: 平均log +0.000760 / 幾何平均 +0.076% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:22:44.467697+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79819.6
- Funnel: target 771 → liquid 180 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +19.03% | $4,276,892.45 |
| FHE/USDT:USDT | +10.85% | $13,911,777.11 |
| LAB/USDT:USDT | +6.47% | $266,167,076.84 |
| PENGUIN/USDT:USDT | +6.44% | $4,619,565.46 |
| BILL/USDT:USDT | +3.48% | $11,350,062.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.45% | +3.50% |
| NOT/USDT:USDT | below_1h_threshold | +3.12% | +3.17% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.97% | +3.02% |
| DOGS/USDT:USDT | below_1h_threshold | +2.63% | +2.69% |
| STRK/USDT:USDT | below_1h_threshold | +2.45% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
