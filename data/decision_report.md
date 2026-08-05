# Decision Report

- generated_at: 2026-08-05T07:16:20.641922+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10375**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10375, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.29% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.33% | **+2.85%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.89% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.78% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.57** / 初期 $100.00 (+517.57%)
- 確定: 3765件 (Win 1195 / Loss 1232 / Flat 1338) / skip 3171件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $617.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.54** / 初期 $100.00 (+44.54%)
- 確定: 1308件 (Win 369 / Loss 305 / Flat 634) / skip 2478件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1088 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $144.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.00** / 初期 $100.00 (+19.00%)
- 確定: 1123件 (Win 361 / Loss 432 / Flat 330) / pending 6件 / skip 721件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.00

## 6. Latest Market Context

- 更新: 2026-08-05T07:16:13.095900+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64143.1
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +64.83% | $1,802,048.54 |
| BLESS/USDT:USDT | +58.05% | $26,586,208.26 |
| HEI/USDT:USDT | +49.69% | $15,485,754.34 |
| BICO/USDT:USDT | +37.41% | $16,901,247.71 |
| SYN/USDT:USDT | +35.09% | $2,962,348.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAKE/USDT:USDT | below_1h_threshold | +2.96% | +3.09% |
| UAI/USDT:USDT | below_1h_threshold | +2.27% | +2.40% |
| CAP/USDT:USDT | below_1h_threshold | +1.67% | +1.80% |
| UNITREE/USDT:USDT | below_1h_threshold | +1.19% | +1.32% |
| BEAT/USDT:USDT | below_1h_threshold | +1.03% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
