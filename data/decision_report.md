# Decision Report

- generated_at: 2026-10-25T05:31:19.173720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17405**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17405, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.59% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_BB3S | 2/19 | 10.5% | +2.00% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.63% | **+1.45%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.92% | **+1.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,480.82** / 初期 $100.00 (+1380.82%)
- 確定: 6658件 (Win 1933 / Loss 2122 / Flat 2603) / skip 7308件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,480.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$306.28** / 初期 $100.00 (+206.28%)
- 確定: 3948件 (Win 1091 / Loss 926 / Flat 1931) / skip 6868件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1713 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $306.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5565件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000593 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T05:31:06.424714+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80794.0
- Funnel: target 1079 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +90.93% | $3,659,851.41 |
| T/USDT:USDT | +30.20% | $3,018,672.08 |
| USELESS/USDT:USDT | +21.29% | $4,082,389.16 |
| LIGHT/USDT:USDT | +18.76% | $1,331,937.61 |
| AGT/USDT:USDT | +17.40% | $5,679,200.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIGHT/USDT:USDT | below_1h_threshold | +2.48% | +2.60% |
| DNA/USDT:USDT | below_1h_threshold | +1.85% | +1.97% |
| USELESS/USDT:USDT | below_1h_threshold | +0.75% | +0.88% |
| INJ/USDT:USDT | below_1h_threshold | +0.64% | +0.76% |
| QNT/USDT:USDT | below_1h_threshold | +0.53% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
