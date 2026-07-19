# Decision Report

- generated_at: 2026-07-19T16:56:33.825939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9056**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=9056, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.76% | **+1.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.52% | **+0.70%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.85% | **+1.45%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.85% | **+1.43%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.09% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.28** / 初期 $100.00 (+299.28%)
- 確定: 3118件 (Win 979 / Loss 997 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $399.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.90** / 初期 $100.00 (+25.90%)
- 確定: 1017件 (Win 263 / Loss 217 / Flat 537) / skip 1450件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0572 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.82** / 初期 $100.00 (+0.82%)
- 確定: 256件 (Win 88 / Loss 128 / Flat 40) / pending 6件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.82

## 6. Latest Market Context

- 更新: 2026-07-19T16:56:19.059015+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64506.0
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1, 4h RSI 78.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +12.75% | $59,571,246.69 |
| TLM/USDT:USDT | +10.07% | $11,868,676.31 |
| ESPORTS/USDT:USDT | +9.82% | $64,553,074.92 |
| DEXE/USDT:USDT | +6.15% | $1,402,781.91 |
| SYN/USDT:USDT | +4.93% | $3,627,248.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +3.24% | +3.30% |
| BLESS/USDT:USDT | below_1h_threshold | +2.65% | +2.71% |
| VANRY/USDT:USDT | below_1h_threshold | +2.42% | +2.48% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.03% | +2.10% |
| SLX/USDT:USDT | below_1h_threshold | +1.61% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
