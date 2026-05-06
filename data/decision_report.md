# Decision Report

- generated_at: 2026-05-06T15:17:36.512420+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3477**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=3477, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.49% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 29件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T15:17:33.650374+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81575.1
- Funnel: target 770 → liquid 196 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +114.90% | $5,038,533.66 |
| LAB/USDT:USDT | +46.07% | $169,948,914.58 |
| BILL/USDT:USDT | +35.46% | $6,026,991.12 |
| ZEC/USDT:USDT | +34.74% | $758,114,593.32 |
| IO/USDT:USDT | +33.58% | $15,524,408.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +5.00% | +4.87% |
| LAB/USDT:USDT | below_1h_threshold | +3.44% | +3.32% |
| ICP/USDT:USDT | below_1h_threshold | +2.69% | +2.56% |
| BILL/USDT:USDT | below_1h_threshold | +2.26% | +2.13% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.25% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
