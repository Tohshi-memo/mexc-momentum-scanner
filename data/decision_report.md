# Decision Report

- generated_at: 2026-05-19T00:53:30.082728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4457**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4457, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.67% | **+1.26%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.58% | **+0.46%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.52% | **+0.44%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.91% | **+0.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.36% | **+1.02%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.32% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.09** / 初期 $100.00 (+21.09%)
- 確定: 454件 (Win 119 / Loss 156 / Flat 179) / skip 564件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $121.09

## 4. Latest Market Context

- 更新: 2026-05-19T00:53:28.067785+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=77205.8
- Funnel: target 765 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +37.28% | $7,646,187.03 |
| INJ/USDT:USDT | +16.67% | $21,807,721.57 |
| ONDO/USDT:USDT | +13.10% | $43,398,064.53 |
| AKT/USDT:USDT | +9.08% | $1,479,468.84 |
| NEAR/USDT:USDT | +7.85% | $9,243,205.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +4.77% | +4.45% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.66% | +2.34% |
| NOWSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.08% |
| RAVE/USDT:USDT | below_1h_threshold | +2.31% | +2.00% |
| OPENLEDGER/USDT:USDT | below_1h_threshold | +2.31% | +1.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
