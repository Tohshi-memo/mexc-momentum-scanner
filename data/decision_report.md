# Decision Report

- generated_at: 2026-07-25T01:36:17.772735+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9472**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.74% / filled 20/20。**
- 全期間 MARKET基準: n=9472, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.70% | **+1.28%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.97% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.31% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.83** / 初期 $100.00 (+4.83%)
- 確定トレード: 137件 (TP 46 / SL 86 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2707件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1718件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0068 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$103.62** / 初期 $100.00 (+3.62%)
- 確定: 524件 (Win 173 / Loss 206 / Flat 145) / pending 5件 / skip 416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $103.62

## 6. Latest Market Context

- 更新: 2026-07-25T01:36:10.840590+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64089.3
- Funnel: target 898 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +27.94% | $46,172,830.68 |
| ACE/USDT:USDT | +23.21% | $8,562,673.41 |
| SLX/USDT:USDT | +13.98% | $1,914,349.86 |
| SAGA/USDT:USDT | +12.77% | $1,156,387.03 |
| PONS/USDT:USDT | +11.09% | $1,224,849.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +3.09% | +3.03% |
| VELVET/USDT:USDT | below_1h_threshold | +2.68% | +2.62% |
| B2/USDT:USDT | below_1h_threshold | +1.53% | +1.47% |
| AKE/USDT:USDT | below_1h_threshold | +1.15% | +1.08% |
| EVAA/USDT:USDT | below_1h_threshold | +1.10% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
