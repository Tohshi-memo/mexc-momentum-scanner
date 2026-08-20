# Decision Report

- generated_at: 2026-08-20T17:31:36.784216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12064**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12064, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.28% | **-0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.94% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.14% | **+1.50%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.84% | **+1.01%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.62%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.40% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$597.96** / 初期 $100.00 (+497.96%)
- 確定: 4277件 (Win 1307 / Loss 1398 / Flat 1572) / skip 4348件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $597.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3653件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.32** / 初期 $100.00 (+16.32%)
- 確定: 1760件 (Win 522 / Loss 674 / Flat 564) / pending 3件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000056 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.32

## 6. Latest Market Context

- 更新: 2026-08-20T17:31:23.656174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=72808.3
- Funnel: target 1011 → liquid 202 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +25.02% | $1,024,757.62 |
| PEOPLE/USDT:USDT | +10.23% | $1,662,170.98 |
| BEAT/USDT:USDT | +9.11% | $36,867,006.28 |
| ONG/USDT:USDT | +8.15% | $4,464,597.66 |
| ALLO/USDT:USDT | +8.11% | $2,727,827.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +4.38% | +4.37% |
| ALLO/USDT:USDT | below_1h_threshold | +3.52% | +3.51% |
| FET/USDT:USDT | below_1h_threshold | +3.10% | +3.09% |
| XLM/USDT:USDT | below_1h_threshold | +2.47% | +2.46% |
| ENA/USDT:USDT | below_1h_threshold | +2.22% | +2.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
