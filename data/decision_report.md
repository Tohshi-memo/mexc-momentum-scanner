# Decision Report

- generated_at: 2026-06-03T22:09:33.527343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5581**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=5581, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.39% | **+1.39%** |
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_BB3S | 2/11 | 18.2% | +5.06% | **+0.92%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.52% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.67% | **+1.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.38% | **+1.24%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.72% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1138件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T22:09:31.109434+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=65487.2
- Funnel: target 767 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +58.41% | $17,197,713.04 |
| STO/USDT:USDT | +24.31% | $5,937,759.56 |
| BP/USDT:USDT | +13.80% | $1,502,359.80 |
| US/USDT:USDT | +8.05% | $5,319,672.40 |
| MAGMA/USDT:USDT | +7.32% | $4,101,344.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STO/USDT:USDT | below_1h_threshold | +2.42% | +2.80% |
| LIT/USDT:USDT | below_1h_threshold | +0.87% | +1.25% |
| BSB/USDT:USDT | below_1h_threshold | +0.56% | +0.94% |
| WIF/USDT:USDT | below_1h_threshold | +0.47% | +0.85% |
| XMR/USDT:USDT | below_1h_threshold | +0.44% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
