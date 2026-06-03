# Decision Report

- generated_at: 2026-06-03T20:28:39.685127+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5578**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=5578, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.52% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.56% | **+1.94%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.45% | **+1.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.86% | **+0.77%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.39% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1135件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T20:28:36.894656+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=65554.6
- Funnel: target 768 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +54.28% | $14,164,073.11 |
| STO/USDT:USDT | +34.95% | $4,964,264.03 |
| BP/USDT:USDT | +10.26% | $1,482,590.56 |
| BEAT/USDT:USDT | +9.85% | $7,780,853.22 |
| RAVE/USDT:USDT | +8.12% | $2,483,989.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.84% | +3.65% |
| LIT/USDT:USDT | below_1h_threshold | +2.72% | +2.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.42% | +2.22% |
| WLD/USDT:USDT | below_1h_threshold | +2.05% | +1.86% |
| SPX/USDT:USDT | below_1h_threshold | +1.73% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
