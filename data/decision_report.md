# Decision Report

- generated_at: 2026-10-01T15:11:49.221461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15915**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15915, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.27% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.33% | **+0.46%** |
| LIMIT_BB3S | 3/13 | 23.1% | +1.40% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.28% | **+1.21%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.43% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.18% | **+0.83%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,300.95** / 初期 $100.00 (+1200.95%)
- 確定: 6026件 (Win 1785 / Loss 1939 / Flat 2302) / skip 6450件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,300.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.04** / 初期 $100.00 (+178.04%)
- 確定: 3568件 (Win 993 / Loss 822 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1316 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $278.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4077件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000438 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T15:11:33.257570+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=83898.0
- Funnel: target 1097 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +77.59% | $7,664,502.50 |
| MOVR/USDT:USDT | +44.76% | $21,375,708.57 |
| CAP/USDT:USDT | +29.83% | $1,195,367.34 |
| ACNSTOCK/USDT:USDT | +19.34% | $1,945,637.22 |
| CT/USDT:USDT | +17.19% | $7,266,571.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.30% | +4.43% |
| ONE/USDT:USDT | below_1h_threshold | +2.07% | +2.20% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.21% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.18% |
| TESLA/USDT:USDT | below_1h_threshold | +0.78% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
