# Decision Report

- generated_at: 2026-11-02T12:36:15.785112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18026**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=18026, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.01% | **+0.51%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.15% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.17% | **+1.30%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.74% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,551.26** / 初期 $100.00 (+1451.26%)
- 確定: 6878件 (Win 1995 / Loss 2206 / Flat 2677) / skip 7709件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,551.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$383.32** / 初期 $100.00 (+283.32%)
- 確定: 4466件 (Win 1199 / Loss 993 / Flat 2274) / skip 6971件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0579 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $383.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6185件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T12:36:05.280743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77840.9
- Funnel: target 1088 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +44.72% | $2,779,003.86 |
| LYN/USDT:USDT | +35.49% | $3,070,072.41 |
| EVAA/USDT:USDT | +16.70% | $4,837,250.34 |
| KORU/USDT:USDT | +9.88% | $46,946,645.92 |
| SOPH/USDT:USDT | +7.81% | $1,066,043.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +1.98% | +2.01% |
| UNI/USDT:USDT | below_1h_threshold | +0.95% | +0.97% |
| SPX/USDT:USDT | below_1h_threshold | +0.59% | +0.62% |
| OP/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| NGAS/USDT:USDT | below_1h_threshold | +0.41% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
