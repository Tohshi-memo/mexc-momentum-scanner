# Decision Report

- generated_at: 2026-11-09T16:31:26.013751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18545**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18545, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 3/20 | 15.0% | -2.35% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.97% | **+2.52%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.43% | **+1.46%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.64% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7163件 (Win 2057 / Loss 2285 / Flat 2821) / skip 7943件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RITUAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7199件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1152 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6713件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000416 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T16:31:15.113476+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=74872.1
- Funnel: target 1094 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +6.08% | $4,678,906.12 |
| SOXS/USDT:USDT | +4.04% | $23,187,541.73 |
| EDGE/USDT:USDT | +2.34% | $2,508,228.79 |
| MRNASTOCK/USDT:USDT | +1.98% | $2,460,658.77 |
| PIEVERSE/USDT:USDT | +1.66% | $5,782,132.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRNASTOCK/USDT:USDT | below_1h_threshold | +3.02% | +3.85% |
| DELTAELECSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +3.76% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +3.20% |
| EDGE/USDT:USDT | below_1h_threshold | +2.34% | +3.18% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.90% | +2.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
