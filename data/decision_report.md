# Decision Report

- generated_at: 2026-08-21T16:46:49.523254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12221, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +2.69% | **+1.24%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.24% | **+0.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.54% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.41% | **+1.08%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4362件 (Win 1337 / Loss 1434 / Flat 1591) / skip 4420件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.47** / 初期 $100.00 (+57.47%)
- 確定: 1834件 (Win 508 / Loss 431 / Flat 895) / skip 3798件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $157.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1880件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T16:46:30.161991+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77301.4
- Funnel: target 1018 → liquid 213 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1, 4h RSI 78.8 >= 65=1, 4h RSI 83.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +33.01% | $10,104,187.64 |
| BEAT/USDT:USDT | +15.27% | $55,292,576.82 |
| PROM/USDT:USDT | +13.06% | $2,284,208.37 |
| BICO/USDT:USDT | +6.32% | $2,653,238.39 |
| AVAAI/USDT:USDT | +5.99% | $2,244,826.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +4.73% | +4.62% |
| BTW/USDT:USDT | below_1h_threshold | +4.73% | +4.62% |
| LAB/USDT:USDT | below_1h_threshold | +4.50% | +4.40% |
| H/USDT:USDT | below_1h_threshold | +4.49% | +4.39% |
| HEMI/USDT:USDT | below_1h_threshold | +4.11% | +4.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
