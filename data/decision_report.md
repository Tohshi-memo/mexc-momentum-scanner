# Decision Report

- generated_at: 2026-05-23T06:14:02.835256+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4757**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4757, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.50% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.46% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.57** / 初期 $100.00 (+22.57%)
- 確定: 603件 (Win 149 / Loss 192 / Flat 262) / skip 715件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $122.57

## 4. Latest Market Context

- 更新: 2026-05-23T06:14:00.752821+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=75438.3
- Funnel: target 764 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +126.69% | $61,568,757.48 |
| IN/USDT:USDT | +23.03% | $1,689,290.40 |
| MYX/USDT:USDT | +12.01% | $1,374,369.97 |
| BILL/USDT:USDT | +10.81% | $18,180,410.51 |
| BEAT/USDT:USDT | +10.31% | $60,831,731.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.11% | +2.12% |
| MYX/USDT:USDT | below_1h_threshold | +1.21% | +1.22% |
| H/USDT:USDT | below_1h_threshold | +0.85% | +0.86% |
| WLFI/USDT:USDT | below_1h_threshold | +0.33% | +0.34% |
| RAVE/USDT:USDT | below_1h_threshold | +0.32% | +0.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
