# Decision Report

- generated_at: 2026-07-19T17:36:10.980966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9060**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=9060, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +3.49% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.87% | **+1.03%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.14% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$110.25** / 初期 $100.00 (+10.25%)
- 確定トレード: 118件 (TP 43 / SL 70 / EXP 5)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $110.25
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.26** / 初期 $100.00 (+299.26%)
- 確定: 3122件 (Win 981 / Loss 999 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $399.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.55** / 初期 $100.00 (+25.55%)
- 確定: 1021件 (Win 264 / Loss 218 / Flat 539) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0792 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.81** / 初期 $100.00 (+0.81%)
- 確定: 260件 (Win 90 / Loss 130 / Flat 40) / pending 3件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.81

## 6. Latest Market Context

- 更新: 2026-07-19T17:36:04.422916+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64673.6
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +20.52% | $59,370,312.18 |
| ESPORTS/USDT:USDT | +9.12% | $64,429,588.10 |
| DEXE/USDT:USDT | +7.88% | $1,460,992.75 |
| TLM/USDT:USDT | +6.89% | $12,055,475.15 |
| SYN/USDT:USDT | +6.75% | $3,589,169.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.10% | +3.85% |
| B/USDT:USDT | below_1h_threshold | +2.42% | +2.17% |
| SYN/USDT:USDT | below_1h_threshold | +2.30% | +2.04% |
| ALLO/USDT:USDT | below_1h_threshold | +1.82% | +1.57% |
| DEXE/USDT:USDT | below_1h_threshold | +1.75% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
