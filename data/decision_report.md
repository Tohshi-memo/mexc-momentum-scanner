# Decision Report

- generated_at: 2026-06-03T08:27:53.879156+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5534**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5534, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.71% | **+1.28%** |
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.51%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.67% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.94** / 初期 $100.00 (+28.94%)
- 確定: 988件 (Win 232 / Loss 306 / Flat 450) / skip 1107件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $128.94

## 4. Latest Market Context

- 更新: 2026-06-03T08:27:48.214626+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=66999.5
- Funnel: target 771 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +38.97% | $14,544,202.45 |
| CLO/USDT:USDT | +36.69% | $3,469,651.01 |
| GENIUS/USDT:USDT | +29.29% | $1,860,222.54 |
| ENA/USDT:USDT | +24.03% | $48,879,741.92 |
| APR/USDT:USDT | +23.04% | $1,358,488.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.67% | +2.95% |
| BEAT/USDT:USDT | below_1h_threshold | +2.01% | +2.29% |
| LIT/USDT:USDT | below_1h_threshold | +1.93% | +2.21% |
| APR/USDT:USDT | below_1h_threshold | +1.27% | +1.55% |
| ONDO/USDT:USDT | below_1h_threshold | +1.27% | +1.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
