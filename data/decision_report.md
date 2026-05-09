# Decision Report

- generated_at: 2026-05-09T16:12:39.105542+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3895**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3895, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +3.54% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.66% | **+0.49%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.67% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.79% | **+1.25%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.82%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.27% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 261件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T16:12:35.952978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80532.5
- Funnel: target 769 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +9.49% | $21,052,743.76 |
| BSB/USDT:USDT | +3.63% | $29,893,515.00 |
| INX/USDT:USDT | +2.86% | $2,232,826.53 |
| RAVE/USDT:USDT | +2.79% | $14,142,130.88 |
| ANTHROPIC/USDT:USDT | +2.61% | $1,292,453.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.76% | +3.71% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.95% | +2.89% |
| INX/USDT:USDT | below_1h_threshold | +2.86% | +2.81% |
| RAVE/USDT:USDT | below_1h_threshold | +2.71% | +2.66% |
| UAI/USDT:USDT | below_1h_threshold | +2.20% | +2.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
