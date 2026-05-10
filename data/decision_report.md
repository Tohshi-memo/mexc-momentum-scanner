# Decision Report

- generated_at: 2026-05-10T02:22:38.609787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3934**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3934, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +1.44% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.34% | **+1.17%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.67% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 299件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T02:22:33.373208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80617.2
- Funnel: target 769 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +36.07% | $6,098,982.49 |
| INX/USDT:USDT | +27.78% | $13,548,139.64 |
| LAYER/USDT:USDT | +22.50% | $1,041,892.19 |
| BIO/USDT:USDT | +13.12% | $1,580,678.31 |
| BRETT/USDT:USDT | +11.39% | $2,564,492.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +2.57% | +2.62% |
| BIO/USDT:USDT | below_1h_threshold | +2.15% | +2.20% |
| BASED/USDT:USDT | below_1h_threshold | +2.14% | +2.19% |
| ORDI/USDT:USDT | below_1h_threshold | +2.06% | +2.11% |
| ZEC/USDT:USDT | below_1h_threshold | +1.55% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
