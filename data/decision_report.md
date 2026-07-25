# Decision Report

- generated_at: 2026-07-25T02:11:19.740102+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9473**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=9473, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.47% | **+1.18%** |
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.51% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.97% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.65% | **+1.33%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.31% | **+0.43%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.83** / 初期 $100.00 (+4.83%)
- 確定トレード: 137件 (TP 46 / SL 86 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2708件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1719件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0676 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$103.62** / 初期 $100.00 (+3.62%)
- 確定: 524件 (Win 173 / Loss 206 / Flat 145) / pending 6件 / skip 416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000186 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $103.62

## 6. Latest Market Context

- 更新: 2026-07-25T02:11:10.498702+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64055.9
- Funnel: target 898 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +34.95% | $46,325,737.30 |
| ACE/USDT:USDT | +18.58% | $8,891,020.29 |
| SLX/USDT:USDT | +16.00% | $1,980,950.83 |
| SAGA/USDT:USDT | +10.62% | $1,193,507.24 |
| ZAMA/USDT:USDT | +9.66% | $3,186,288.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +2.23% | +2.20% |
| B2/USDT:USDT | below_1h_threshold | +1.55% | +1.53% |
| SLX/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| AKE/USDT:USDT | below_1h_threshold | +0.71% | +0.68% |
| TLM/USDT:USDT | below_1h_threshold | +0.70% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
