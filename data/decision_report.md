# Decision Report

- generated_at: 2026-10-22T06:31:31.172091+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17116**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17116, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.40% | **+0.34%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.31% | **+0.92%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.36% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,344.58** / 初期 $100.00 (+1244.58%)
- 確定: 6498件 (Win 1890 / Loss 2073 / Flat 2535) / skip 7179件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,344.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.50** / 初期 $100.00 (+178.50%)
- 確定: 3826件 (Win 1051 / Loss 895 / Flat 1880) / skip 6701件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0543 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $278.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5277件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T06:31:16.654072+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=82590.1
- Funnel: target 1090 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +37.82% | $1,190,946.18 |
| BTW/USDT:USDT | +16.43% | $31,959,033.88 |
| PHA/USDT:USDT | +15.23% | $4,649,677.69 |
| AGT/USDT:USDT | +13.66% | $5,719,849.82 |
| SOXS/USDT:USDT | +9.91% | $10,996,897.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RUNE/USDT:USDT | below_1h_threshold | +4.12% | +4.35% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.69% | +3.92% |
| PHA/USDT:USDT | below_1h_threshold | +2.32% | +2.55% |
| AGT/USDT:USDT | below_1h_threshold | +2.31% | +2.54% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.30% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
