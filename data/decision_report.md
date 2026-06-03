# Decision Report

- generated_at: 2026-06-03T08:22:23.106598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5532**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5532, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.47% | **+1.18%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.57% | **+0.46%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.46% | **+0.42%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.27% | **+0.70%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.10% | **+0.04%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.18% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.59** / 初期 $100.00 (+29.59%)
- 確定: 986件 (Win 232 / Loss 305 / Flat 449) / skip 1107件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $129.59

## 4. Latest Market Context

- 更新: 2026-06-03T08:22:17.852274+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=66995.5
- Funnel: target 771 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +38.76% | $3,414,969.37 |
| PORTAL/USDT:USDT | +38.71% | $14,503,831.07 |
| GENIUS/USDT:USDT | +27.68% | $1,852,936.54 |
| APR/USDT:USDT | +25.35% | $1,353,327.57 |
| ENA/USDT:USDT | +23.93% | $48,760,805.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.24% | +3.53% |
| RIF/USDT:USDT | below_1h_threshold | +2.72% | +3.00% |
| BEAT/USDT:USDT | below_1h_threshold | +2.63% | +2.92% |
| MYX/USDT:USDT | below_1h_threshold | +2.28% | +2.56% |
| US/USDT:USDT | below_1h_threshold | +2.05% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
