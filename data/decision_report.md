# Decision Report

- generated_at: 2026-09-02T14:51:15.452465+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13340**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13340, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.22% | **+0.31%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.11% | **+0.07%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.89% | **+1.61%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.01% | **+1.51%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.05% | **+1.12%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.52% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$846.97** / 初期 $100.00 (+746.97%)
- 確定: 4966件 (Win 1506 / Loss 1628 / Flat 1832) / skip 4935件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $846.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.37** / 初期 $100.00 (+75.37%)
- 確定: 2319件 (Win 646 / Loss 555 / Flat 1118) / skip 4432件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0519 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $175.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2717件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T14:51:05.926013+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77191.2
- Funnel: target 1044 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +43.74% | $14,284,147.28 |
| MAGMA/USDT:USDT | +41.59% | $12,270,033.77 |
| FONE/USDT:USDT | +39.08% | $1,957,477.52 |
| BULLA/USDT:USDT | +17.36% | $1,000,259.15 |
| PYTH/USDT:USDT | +13.14% | $4,052,349.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARB/USDT:USDT | below_1h_threshold | +4.85% | +4.74% |
| PYTH/USDT:USDT | below_1h_threshold | +3.32% | +3.22% |
| BULLA/USDT:USDT | below_1h_threshold | +3.07% | +2.97% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.95% | +2.85% |
| ASTER/USDT:USDT | below_1h_threshold | +2.78% | +2.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
