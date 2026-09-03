# Decision Report

- generated_at: 2026-09-03T16:11:32.732207+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13500, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.05% | **-2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |
| LIMIT_8PCT | 3/20 | 15.0% | -1.43% | **-0.21%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.74% | **-0.26%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |
| LIMIT_6PCT | 3/20 | 15.0% | -2.04% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.68% | **+1.87%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +4.66% | **+1.86%** |
| MARKET_LONG | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.65% | **+1.82%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5053件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4538件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1869 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.20** / 初期 $100.00 (+17.20%)
- 確定: 2182件 (Win 652 / Loss 853 / Flat 677) / pending 4件 / skip 2791件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000531 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.20

## 6. Latest Market Context

- 更新: 2026-09-03T16:11:23.173121+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=80969.9
- Funnel: target 1046 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +5.01% | $2,309,577.54 |
| FONE/USDT:USDT | +4.51% | $1,080,568.67 |
| BR/USDT:USDT | +1.80% | $7,644,792.93 |
| BULLA/USDT:USDT | +1.31% | $9,907,133.87 |
| MARSCOIN/USDT:USDT | +1.23% | $9,256,640.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_1h_threshold | +4.57% | +5.00% |
| FONE/USDT:USDT | below_1h_threshold | +4.51% | +4.94% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.08% | +4.50% |
| KORU/USDT:USDT | below_1h_threshold | +2.12% | +2.54% |
| BR/USDT:USDT | below_1h_threshold | +1.96% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
