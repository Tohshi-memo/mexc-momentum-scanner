# Decision Report

- generated_at: 2026-09-06T02:56:34.918525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13790**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13790, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.88% | **+0.18%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.09% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.43% | **+1.07%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +1.58% | **+0.79%** |
| MARKET_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$867.29** / 初期 $100.00 (+767.29%)
- 確定: 5096件 (Win 1530 / Loss 1662 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $867.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.01** / 初期 $100.00 (+90.01%)
- 確定: 2535件 (Win 707 / Loss 600 / Flat 1228) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0550 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $190.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.10** / 初期 $100.00 (+20.10%)
- 確定: 2407件 (Win 717 / Loss 913 / Flat 777) / pending 5件 / skip 2854件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.10

## 6. Latest Market Context

- 更新: 2026-09-06T02:56:20.462343+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=79859.0
- Funnel: target 1050 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 73.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +42.71% | $111,660,971.93 |
| UAI/USDT:USDT | +38.43% | $8,368,016.14 |
| FLOCK/USDT:USDT | +28.00% | $1,063,462.29 |
| BASECAT/USDT:USDT | +24.23% | $2,073,824.84 |
| SUSHI/USDT:USDT | +19.68% | $4,249,719.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.08% | +3.15% |
| HNT/USDT:USDT | below_1h_threshold | +2.72% | +2.79% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.47% | +2.54% |
| BCH/USDT:USDT | below_1h_threshold | +1.47% | +1.54% |
| MONAD/USDT:USDT | below_1h_threshold | +0.78% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
