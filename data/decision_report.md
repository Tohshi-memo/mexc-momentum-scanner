# Decision Report

- generated_at: 2026-05-04T18:42:20.120353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3249**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=3249, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.22% | **+1.16%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.69% | **+1.08%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.24% | **+0.74%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T18:42:15.491097+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80186.5
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.9 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +14.19% | $42,506,567.04 |
| RAVE/USDT:USDT | +11.44% | $14,446,047.85 |
| TST/USDT:USDT | +9.67% | $22,016,396.93 |
| USTC/USDT:USDT | +9.05% | $1,200,072.16 |
| FHE/USDT:USDT | +7.20% | $2,859,178.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +3.49% | +3.68% |
| M/USDT:USDT | below_1h_threshold | +2.96% | +3.15% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.51% | +1.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.13% | +1.32% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.84% | +1.04% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
