# Decision Report

- generated_at: 2026-06-10T15:48:57.011126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6225**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6225, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.94% | **+0.19%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -1.10% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.75% | **+0.87%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1557件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T15:48:50.843296+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=62268.0
- Funnel: target 785 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STRAX/USDT:USDT | +48.69% | $1,042,543.57 |
| MAGMA/USDT:USDT | +45.76% | $2,434,489.89 |
| STG/USDT:USDT | +45.42% | $20,707,227.59 |
| ESPORTS/USDT:USDT | +43.82% | $25,727,425.31 |
| HMSTR/USDT:USDT | +42.47% | $2,349,683.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +4.49% | +4.33% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.59% | +1.43% |
| LIT/USDT:USDT | below_1h_threshold | +1.23% | +1.07% |
| USOIL/USDT:USDT | below_1h_threshold | +0.69% | +0.53% |
| SPX/USDT:USDT | below_1h_threshold | +0.67% | +0.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
