# Decision Report

- generated_at: 2026-05-14T21:13:00.896801+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4310**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=4310, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +4.71% | **+1.57%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.65% | **+0.82%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.68% | **+0.67%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 363件 (Win 96 / Loss 129 / Flat 138) / skip 508件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRCLSTOCK/USDT:USDT `LIMIT_BB3S` TP_HIT account +1.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-14T21:12:57.722627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81315.7
- Funnel: target 758 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +15.84% | $3,284,468.39 |
| FIGSTOCK/USDT:USDT | +11.00% | $2,440,537.35 |
| TROLLSOL/USDT:USDT | +9.25% | $1,677,071.95 |
| NAORIS/USDT:USDT | +8.41% | $3,097,797.52 |
| LAB/USDT:USDT | +7.18% | $120,038,170.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.38% | +1.45% |
| CC/USDT:USDT | below_1h_threshold | +1.08% | +1.15% |
| BILL/USDT:USDT | below_1h_threshold | +1.06% | +1.13% |
| STAR/USDT:USDT | below_1h_threshold | +0.80% | +0.87% |
| ZEC/USDT:USDT | below_1h_threshold | +0.72% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
