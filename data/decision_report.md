# Decision Report

- generated_at: 2026-06-08T02:14:03.484446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6021**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6021, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.54% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 2/17 | 11.8% | +1.81% | **+0.21%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| ASK_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.91** / 初期 $100.00 (+52.91%)
- 確定: 1138件 (Win 278 / Loss 346 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $152.91

## 4. Latest Market Context

- 更新: 2026-06-08T02:14:00.942240+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63110.0
- Funnel: target 773 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +33.15% | $91,298,219.64 |
| EPIC/USDT:USDT | +28.06% | $1,612,217.12 |
| BANK/USDT:USDT | +25.54% | $4,655,578.20 |
| PIPPIN/USDT:USDT | +23.01% | $6,406,208.74 |
| ALLO/USDT:USDT | +22.21% | $42,268,186.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +2.30% | +2.42% |
| EPIC/USDT:USDT | below_1h_threshold | +1.80% | +1.92% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.42% | +1.54% |
| BABY/USDT:USDT | below_1h_threshold | +1.34% | +1.46% |
| NEAR/USDT:USDT | below_1h_threshold | +1.32% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
