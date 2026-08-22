# Decision Report

- generated_at: 2026-08-22T05:06:36.419085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12323**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12323, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.19% | **+1.13%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.42% | **+0.85%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.59% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.23%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.16% | **+1.19%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$737.94** / 初期 $100.00 (+637.94%)
- 確定: 4441件 (Win 1364 / Loss 1447 / Flat 1630) / skip 4443件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WLFI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.66% 残高後 $737.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.30** / 初期 $100.00 (+59.30%)
- 確定: 1929件 (Win 533 / Loss 460 / Flat 936) / skip 3805件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2304 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: WLFI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.44% 残高後 $159.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.28** / 初期 $100.00 (+18.28%)
- 確定: 1856件 (Win 549 / Loss 699 / Flat 608) / pending 6件 / skip 1947件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000479 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.28

## 6. Latest Market Context

- 更新: 2026-08-22T05:06:24.927458+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78517.6
- Funnel: target 1018 → liquid 220 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.4 >= 65=1, 4h RSI 83.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +242.26% | $4,529,681.76 |
| TRUMPOFFICIAL/USDT:USDT | +83.60% | $59,866,935.19 |
| CATE/USDT:USDT | +78.71% | $11,368,525.65 |
| MUBARAK/USDT:USDT | +41.33% | $1,591,694.28 |
| ZAMA/USDT:USDT | +28.06% | $1,079,488.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +2.98% | +2.93% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.44% | +2.39% |
| CATE/USDT:USDT | below_1h_threshold | +2.30% | +2.25% |
| RE/USDT:USDT | below_1h_threshold | +1.99% | +1.93% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.97% | +1.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
