# Decision Report

- generated_at: 2026-07-19T07:26:11.560936+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9009**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9009, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +1.51% | **+0.30%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.02% | **+0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_BB3S | 2/17 | 11.8% | -0.88% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.91% | **+2.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.08% | **+1.15%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$392.35** / 初期 $100.00 (+292.35%)
- 確定: 3071件 (Win 961 / Loss 977 / Flat 1133) / skip 2499件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $392.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.59** / 初期 $100.00 (+25.59%)
- 確定: 970件 (Win 247 / Loss 197 / Flat 526) / skip 1450件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $125.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.08** / 初期 $100.00 (+0.08%)
- 確定: 212件 (Win 67 / Loss 109 / Flat 36) / pending 4件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000587 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.08

## 6. Latest Market Context

- 更新: 2026-07-19T07:26:06.337171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64691.9
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +137.51% | $41,102,327.06 |
| TLM/USDT:USDT | +47.58% | $4,243,462.86 |
| BANK/USDT:USDT | +35.15% | $17,499,165.38 |
| B/USDT:USDT | +31.02% | $38,987,766.54 |
| BULLA/USDT:USDT | +21.13% | $1,230,275.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.40% | +3.38% |
| KAITO/USDT:USDT | below_1h_threshold | +1.25% | +1.24% |
| BILL/USDT:USDT | below_1h_threshold | +1.24% | +1.23% |
| RE/USDT:USDT | below_1h_threshold | +0.93% | +0.92% |
| VVV/USDT:USDT | below_1h_threshold | +0.78% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
