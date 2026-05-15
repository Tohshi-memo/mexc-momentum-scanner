# Decision Report

- generated_at: 2026-05-15T21:18:24.079720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4350**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4350, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_BB3S | 8/13 | 61.5% | +0.77% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.03% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 521件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T21:18:18.391326+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79144.6
- Funnel: target 759 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +26.05% | $2,915,285.00 |
| STORJ/USDT:USDT | +24.37% | $3,745,125.82 |
| LAB/USDT:USDT | +11.72% | $144,399,627.21 |
| PEAQ/USDT:USDT | +7.29% | $5,180,479.50 |
| TROLLSOL/USDT:USDT | +6.52% | $1,063,810.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +4.75% | +4.67% |
| UB/USDT:USDT | below_1h_threshold | +2.31% | +2.23% |
| STORJ/USDT:USDT | below_1h_threshold | +1.76% | +1.68% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.56% | +1.48% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.54% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
