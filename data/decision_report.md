# Decision Report

- generated_at: 2026-06-08T10:01:11.893361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6065**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6065, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.21% | **+0.44%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.33% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.56% | **+1.79%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.93% | **+1.54%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.96% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1482件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T10:01:08.966670+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63510.0
- Funnel: target 777 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +51.54% | $48,267,179.78 |
| BEAT/USDT:USDT | +47.79% | $119,763,973.98 |
| BLESS/USDT:USDT | +34.85% | $9,336,015.62 |
| PIPPIN/USDT:USDT | +32.59% | $12,724,868.50 |
| VELVET/USDT:USDT | +29.96% | $4,228,964.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +0.78% | +0.71% |
| VELVET/USDT:USDT | below_1h_threshold | +0.71% | +0.64% |
| ALLO/USDT:USDT | below_1h_threshold | +0.57% | +0.50% |
| DYDX/USDT:USDT | below_1h_threshold | +0.56% | +0.50% |
| LIT/USDT:USDT | below_1h_threshold | +0.55% | +0.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
