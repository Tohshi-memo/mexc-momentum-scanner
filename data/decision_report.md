# Decision Report

- generated_at: 2026-09-02T15:46:40.679452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13343**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13343, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.34% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.22% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.26% | **+1.81%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.14% | **+1.72%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.16% | **+1.25%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$846.82** / 初期 $100.00 (+746.82%)
- 確定: 4969件 (Win 1506 / Loss 1629 / Flat 1834) / skip 4935件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $846.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.50** / 初期 $100.00 (+75.50%)
- 確定: 2322件 (Win 647 / Loss 556 / Flat 1119) / skip 4432件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0405 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $175.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2722件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T15:46:26.133965+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=77259.7
- Funnel: target 1044 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +48.77% | $2,026,664.58 |
| T/USDT:USDT | +39.90% | $15,227,891.02 |
| MAGMA/USDT:USDT | +39.20% | $13,050,978.02 |
| BULLA/USDT:USDT | +21.17% | $1,131,151.67 |
| CASHCAT/USDT:USDT | +18.42% | $2,062,515.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.84% | +4.53% |
| ZRO/USDT:USDT | below_1h_threshold | +4.14% | +3.84% |
| BULLA/USDT:USDT | below_1h_threshold | +2.77% | +2.46% |
| SEI/USDT:USDT | below_1h_threshold | +2.45% | +2.14% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.87% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
