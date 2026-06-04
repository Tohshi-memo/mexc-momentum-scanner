# Decision Report

- generated_at: 2026-06-04T09:24:47.548873+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5616**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=5616, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| ASK | 20/20 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.39% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.30% | **+0.08%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.32% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1006件 (Win 239 / Loss 312 / Flat 455) / skip 1171件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T09:24:45.206413+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.96% price=62985.1
- Funnel: target 771 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +30.44% | $4,148,255.97 |
| SIREN/USDT:USDT | +22.43% | $4,623,655.54 |
| EPIC/USDT:USDT | +19.22% | $5,264,669.02 |
| OPN/USDT:USDT | +19.20% | $32,276,106.08 |
| LAB/USDT:USDT | +9.74% | $127,090,012.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.78% | +2.74% |
| LAB/USDT:USDT | below_1h_threshold | +0.85% | +1.81% |
| BP/USDT:USDT | below_1h_threshold | +0.56% | +1.52% |
| EDGE/USDT:USDT | below_1h_threshold | +0.38% | +1.34% |
| OPN/USDT:USDT | below_1h_threshold | +0.26% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
