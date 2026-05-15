# Decision Report

- generated_at: 2026-05-15T21:13:31.089013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4349**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4349, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_BB3S | 8/13 | 61.5% | +0.77% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.52% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$97.69** / 初期 $100.00 (-2.31%)
- 確定トレード: 46件 (TP 12 / SL 31 / EXP 3)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 520件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T21:13:25.372288+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79142.6
- Funnel: target 759 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +27.25% | $2,896,906.96 |
| STORJ/USDT:USDT | +23.02% | $3,678,447.67 |
| LAB/USDT:USDT | +13.47% | $143,341,192.00 |
| PEAQ/USDT:USDT | +6.55% | $5,171,230.52 |
| INX/USDT:USDT | +6.13% | $1,093,906.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +4.05% | +3.97% |
| UB/USDT:USDT | below_1h_threshold | +1.45% | +1.37% |
| INX/USDT:USDT | below_1h_threshold | +1.24% | +1.16% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +0.98% | +0.91% |
| PEAQ/USDT:USDT | below_1h_threshold | +0.93% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
