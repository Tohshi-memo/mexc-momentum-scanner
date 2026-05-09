# Decision Report

- generated_at: 2026-05-09T16:17:36.642395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3896**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3896, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +2.28% | **+0.86%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.44% | **+0.29%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.79% | **+1.25%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.82%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.27% | **+0.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 262件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T16:17:33.101491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80589.4
- Funnel: target 769 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1, 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +22.30% | $22,146,311.82 |
| OFC/USDT:USDT | +6.50% | $1,051,588.89 |
| RAVE/USDT:USDT | +3.17% | $14,337,154.60 |
| SIREN/USDT:USDT | +3.16% | $20,417,756.26 |
| BIO/USDT:USDT | +2.98% | $1,259,538.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.45% | +3.32% |
| RAVE/USDT:USDT | below_1h_threshold | +3.38% | +3.26% |
| BIO/USDT:USDT | below_1h_threshold | +2.98% | +2.86% |
| INX/USDT:USDT | below_1h_threshold | +2.79% | +2.66% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.69% | +2.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
