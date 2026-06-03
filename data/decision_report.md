# Decision Report

- generated_at: 2026-06-03T23:07:50.450780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5583**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.31% / filled 20/20。**
- 全期間 MARKET基準: n=5583, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.34% | **+2.34%** |
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.33% | **+1.06%** |
| LIMIT_BB3S | 2/11 | 18.2% | +5.06% | **+0.92%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.15% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.67% | **+1.67%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.35% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1140件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T23:07:48.053980+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=64554.5
- Funnel: target 768 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +37.81% | $19,194,525.70 |
| STO/USDT:USDT | +24.07% | $6,324,287.69 |
| BP/USDT:USDT | +10.54% | $1,521,148.67 |
| MAGMA/USDT:USDT | +7.37% | $4,143,186.98 |
| LIT/USDT:USDT | +6.69% | $8,881,948.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STO/USDT:USDT | below_1h_threshold | +0.98% | +1.49% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.94% | +1.45% |
| GUA/USDT:USDT | below_1h_threshold | +0.69% | +1.20% |
| BSB/USDT:USDT | below_1h_threshold | +0.59% | +1.10% |
| EDGE/USDT:USDT | below_1h_threshold | +0.35% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
