# Decision Report

- generated_at: 2026-05-02T18:22:47.128465+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2967**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=2967, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.58% | **+1.58%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.40% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.90% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T18:22:42.989397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78336.9
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +14.84% | $7,534,641.84 |
| XNY/USDT:USDT | +10.53% | $1,270,541.72 |
| TAC/USDT:USDT | +8.57% | $2,599,548.49 |
| BIANRENSHENG/USDT:USDT | +7.60% | $1,038,429.67 |
| BASED/USDT:USDT | +6.19% | $1,304,368.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLS/USDT:USDT | below_1h_threshold | +3.67% | +3.70% |
| XNY/USDT:USDT | below_1h_threshold | +3.18% | +3.21% |
| LUNC/USDT:USDT | below_1h_threshold | +1.80% | +1.84% |
| VELVET/USDT:USDT | below_1h_threshold | +1.12% | +1.16% |
| ORCA/USDT:USDT | below_1h_threshold | +1.08% | +1.11% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
