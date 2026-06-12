# Decision Report

- generated_at: 2026-06-12T11:17:35.009956+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6504**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=6504, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/17 | 41.2% | +2.35% | **+0.97%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.58% | **+0.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.86% | **+0.56%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.87% | **+3.24%** |
| ASK_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 18件 (TP 2 / SL 15 / EXP 1)
- 最新: MYX/USDT:USDT SL_HIT PnL -3.58% 残高後 $94.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.89** / 初期 $100.00 (+68.89%)
- 確定: 1377件 (Win 378 / Loss 443 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $168.89

## 4. Latest Market Context

- 更新: 2026-06-12T11:17:31.792306+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63780.8
- Funnel: target 774 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +89.16% | $154,551,281.28 |
| ESPORTS/USDT:USDT | +76.08% | $45,055,920.03 |
| NAORIS/USDT:USDT | +46.49% | $5,044,481.14 |
| XPL/USDT:USDT | +39.39% | $12,211,875.37 |
| AIN/USDT:USDT | +35.01% | $1,099,088.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +3.24% | +3.06% |
| AIN/USDT:USDT | below_1h_threshold | +2.61% | +2.43% |
| COAI/USDT:USDT | below_1h_threshold | +2.35% | +2.16% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.25% | +2.07% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.22% | +2.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
