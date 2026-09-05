# Decision Report

- generated_at: 2026-09-05T17:31:28.204930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13761, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.20% | **-0.16%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.85% | **+0.93%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.91** / 初期 $100.00 (+759.91%)
- 確定: 5067件 (Win 1521 / Loss 1652 / Flat 1894) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $859.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.52** / 初期 $100.00 (+88.52%)
- 確定: 2506件 (Win 698 / Loss 590 / Flat 1218) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $188.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.53** / 初期 $100.00 (+19.53%)
- 確定: 2381件 (Win 706 / Loss 903 / Flat 772) / pending 5件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.53

## 6. Latest Market Context

- 更新: 2026-09-05T17:31:16.576754+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80024.0
- Funnel: target 1050 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=2
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +17.92% | $2,426,238.09 |
| 4/USDT:USDT | +15.53% | $24,549,981.59 |
| MAGMA/USDT:USDT | +13.81% | $2,167,394.15 |
| USELESS/USDT:USDT | +13.10% | $20,420,714.04 |
| MARSCOIN/USDT:USDT | +8.03% | $8,906,303.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.52% | +4.49% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.60% | +3.57% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.72% | +2.70% |
| B/USDT:USDT | below_1h_threshold | +2.20% | +2.17% |
| PONS/USDT:USDT | below_1h_threshold | +1.82% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
