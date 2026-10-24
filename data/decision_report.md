# Decision Report

- generated_at: 2026-10-24T07:56:26.155286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17346**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17346, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.34% | **+1.63%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.49% | **+1.26%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,316.03** / 初期 $100.00 (+1216.03%)
- 確定: 6599件 (Win 1909 / Loss 2103 / Flat 2587) / skip 7308件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.50% 残高後 $1,316.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6827件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0985 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5505件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T07:56:10.651475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80725.4
- Funnel: target 1079 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +120.87% | $10,818,470.12 |
| BMT/USDT:USDT | +71.34% | $1,942,877.39 |
| IRYS/USDT:USDT | +29.52% | $103,684,960.72 |
| AGT/USDT:USDT | +15.30% | $9,682,625.08 |
| AXIS/USDT:USDT | +10.49% | $3,165,425.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +3.29% | +3.32% |
| BTW/USDT:USDT | below_1h_threshold | +1.55% | +1.58% |
| DOS/USDT:USDT | below_1h_threshold | +1.46% | +1.49% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.43% | +0.46% |
| WLFI/USDT:USDT | below_1h_threshold | +0.38% | +0.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
