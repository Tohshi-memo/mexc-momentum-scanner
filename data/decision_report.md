# Decision Report

- generated_at: 2026-07-22T12:56:23.923801+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9283**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=9283, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.71% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.66%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.97% | **+0.58%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.83% | **+0.46%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.62** / 初期 $100.00 (+329.62%)
- 確定: 3280件 (Win 1035 / Loss 1054 / Flat 1191) / skip 2564件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $429.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1534件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0912 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.26** / 初期 $100.00 (+2.26%)
- 確定: 419件 (Win 142 / Loss 172 / Flat 105) / pending 4件 / skip 332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000307 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $102.26

## 6. Latest Market Context

- 更新: 2026-07-22T12:56:12.857664+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=65670.2
- Funnel: target 888 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +40.88% | $3,471,236.23 |
| RE/USDT:USDT | +24.38% | $11,486,903.26 |
| AKE/USDT:USDT | +22.58% | $10,908,524.24 |
| UB/USDT:USDT | +15.39% | $1,850,089.31 |
| TLM/USDT:USDT | +15.00% | $2,401,890.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INFQSTOCK/USDT:USDT | below_1h_threshold | +3.37% | +3.84% |
| SOXS/USDT:USDT | below_1h_threshold | +2.05% | +2.52% |
| BNCSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +1.30% |
| JTO/USDT:USDT | below_1h_threshold | +0.80% | +1.27% |
| CMCSASTOCK/USDT:USDT | below_1h_threshold | +0.78% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
