# Decision Report

- generated_at: 2026-10-25T02:36:21.207164+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17391, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.82% | **+0.99%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.13% | **+0.94%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.57% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.02% | **+0.91%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,436.56** / 初期 $100.00 (+1336.56%)
- 確定: 6644件 (Win 1927 / Loss 2118 / Flat 2599) / skip 7308件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,436.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$300.06** / 初期 $100.00 (+200.06%)
- 確定: 3934件 (Win 1085 / Loss 922 / Flat 1927) / skip 6868件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2288 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $300.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5550件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000695 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T02:36:06.266515+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80857.8
- Funnel: target 1079 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +50.55% | $1,830,616.63 |
| APR/USDT:USDT | +18.32% | $1,987,491.79 |
| USELESS/USDT:USDT | +17.12% | $3,497,542.51 |
| LIGHT/USDT:USDT | +16.10% | $1,212,844.72 |
| AGT/USDT:USDT | +14.31% | $5,957,012.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| GRASS/USDT:USDT | below_1h_threshold | +0.55% | +0.57% |
| DNA/USDT:USDT | below_1h_threshold | +0.42% | +0.44% |
| AGT/USDT:USDT | below_1h_threshold | +0.29% | +0.31% |
| QNT/USDT:USDT | below_1h_threshold | +0.22% | +0.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
