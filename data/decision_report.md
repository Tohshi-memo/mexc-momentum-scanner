# Decision Report

- generated_at: 2026-06-09T13:13:55.851213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6137, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.96% | **+0.72%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.19% | **+0.13%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.38** / 初期 $100.00 (+50.38%)
- 確定: 1177件 (Win 295 / Loss 368 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $150.38

## 4. Latest Market Context

- 更新: 2026-06-09T13:13:52.905937+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62528.5
- Funnel: target 774 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +50.54% | $22,652,752.15 |
| SLX/USDT:USDT | +27.80% | $5,526,963.36 |
| POWER/USDT:USDT | +25.44% | $3,292,905.75 |
| PLAY/USDT:USDT | +20.46% | $2,239,299.46 |
| VELVET/USDT:USDT | +14.49% | $21,305,321.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.39% | +3.52% |
| POWER/USDT:USDT | below_1h_threshold | +2.95% | +3.09% |
| BTW/USDT:USDT | below_1h_threshold | +2.10% | +2.23% |
| VELVET/USDT:USDT | below_1h_threshold | +1.89% | +2.02% |
| PLAY/USDT:USDT | below_1h_threshold | +1.77% | +1.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
