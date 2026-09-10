# Decision Report

- generated_at: 2026-09-10T02:31:19.456348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14142**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14142, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +2.75% | **+1.24%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.99% | **+0.40%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.08% | **+2.46%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.27% | **+1.93%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,027.36** / 初期 $100.00 (+927.36%)
- 確定: 5322件 (Win 1599 / Loss 1717 / Flat 2006) / skip 5381件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,027.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$203.24** / 初期 $100.00 (+103.24%)
- 確定: 2736件 (Win 755 / Loss 641 / Flat 1340) / skip 4817件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $203.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定: 2647件 (Win 779 / Loss 1011 / Flat 857) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000478 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.89

## 6. Latest Market Context

- 更新: 2026-09-10T02:31:08.249831+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78007.9
- Funnel: target 1064 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +43.64% | $1,614,699.98 |
| BTR/USDT:USDT | +21.64% | $2,510,244.37 |
| CATE/USDT:USDT | +19.30% | $2,834,245.41 |
| SOXS/USDT:USDT | +2.19% | $2,394,545.52 |
| WLFI/USDT:USDT | +2.02% | $5,218,133.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +1.14% | +1.21% |
| BR/USDT:USDT | below_1h_threshold | +1.08% | +1.15% |
| AKE/USDT:USDT | below_1h_threshold | +1.00% | +1.07% |
| WLFI/USDT:USDT | below_1h_threshold | +0.97% | +1.03% |
| INJ/USDT:USDT | below_1h_threshold | +0.82% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
