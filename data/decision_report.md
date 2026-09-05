# Decision Report

- generated_at: 2026-09-05T17:01:25.572340+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13756**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13756, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.08% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.77% | **+1.53%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.79% | **+1.26%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.59% | **+1.17%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$852.22** / 初期 $100.00 (+752.22%)
- 確定: 5062件 (Win 1520 / Loss 1652 / Flat 1890) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $852.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.71** / 初期 $100.00 (+87.71%)
- 確定: 2501件 (Win 697 / Loss 590 / Flat 1214) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0267 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $187.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 2378件 (Win 705 / Loss 903 / Flat 770) / pending 6件 / skip 2847件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.22

## 6. Latest Market Context

- 更新: 2026-09-05T17:01:15.745140+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79988.7
- Funnel: target 1050 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +15.05% | $23,942,834.76 |
| NIULAI/USDT:USDT | +12.08% | $2,097,249.10 |
| USELESS/USDT:USDT | +10.75% | $19,369,344.20 |
| MAGMA/USDT:USDT | +6.14% | $2,089,767.75 |
| BASECAT/USDT:USDT | +5.24% | $1,975,723.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.25% | +3.27% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.13% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |
| INTUSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.94% |
| EDGE/USDT:USDT | below_1h_threshold | +0.75% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
