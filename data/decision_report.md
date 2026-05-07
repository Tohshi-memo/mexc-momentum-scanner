# Decision Report

- generated_at: 2026-05-07T00:57:39.292241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3516**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3516, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.40% | **+0.14%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.54% | **+0.05%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.24% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.84% | **+1.29%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.63% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.50** / 初期 $100.00 (-1.50%)
- 確定: 12件 (Win 1 / Loss 5 / Flat 6) / skip 65件
- 成長率目線: 平均log -0.001259 / 幾何平均 -0.126% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $98.50

## 4. Latest Market Context

- 更新: 2026-05-07T00:57:33.143471+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=81025.1
- Funnel: target 766 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +26.57% | $5,321,493.58 |
| PLAY/USDT:USDT | +21.84% | $19,099,425.58 |
| ZEREBRO/USDT:USDT | +20.12% | $1,858,039.83 |
| LAB/USDT:USDT | +14.11% | $255,266,093.44 |
| FHE/USDT:USDT | +13.75% | $16,754,823.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.05% | +4.50% |
| VVV/USDT:USDT | below_1h_threshold | +3.61% | +4.06% |
| B/USDT:USDT | below_1h_threshold | +2.06% | +2.51% |
| LYN/USDT:USDT | below_1h_threshold | +1.72% | +2.17% |
| TAG/USDT:USDT | below_1h_threshold | +1.71% | +2.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
