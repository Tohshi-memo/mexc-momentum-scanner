# Decision Report

- generated_at: 2026-05-29T16:19:54.054122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5058**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5058, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 7/13 | 53.8% | +1.05% | **+0.57%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.48% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.15% | **+1.35%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +3.42% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 879件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T16:19:51.335306+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=73712.8
- Funnel: target 777 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +17.33% | $4,574,538.48 |
| BAT/USDT:USDT | +2.12% | $1,943,065.76 |
| BEAT/USDT:USDT | +1.97% | $20,270,855.73 |
| VVV/USDT:USDT | +1.80% | $7,849,483.27 |
| ASTSSTOCK/USDT:USDT | +1.76% | $1,584,605.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +2.12% | +2.21% |
| BEAT/USDT:USDT | below_1h_threshold | +1.98% | +2.06% |
| VVV/USDT:USDT | below_1h_threshold | +1.81% | +1.89% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +1.77% | +1.86% |
| RAVE/USDT:USDT | below_1h_threshold | +1.40% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
