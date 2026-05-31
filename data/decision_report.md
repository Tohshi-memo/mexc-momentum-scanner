# Decision Report

- generated_at: 2026-05-31T14:00:05.485641+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5194**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5194, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_BB3S | 5/14 | 35.7% | +1.06% | **+0.38%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.23%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.88%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$98.58** / 初期 $100.00 (-1.42%)
- 確定トレード: 80件 (TP 24 / SL 53 / EXP 3)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.14** / 初期 $100.00 (+26.14%)
- 確定: 829件 (Win 190 / Loss 247 / Flat 392) / skip 926件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.86% 残高後 $126.14

## 4. Latest Market Context

- 更新: 2026-05-31T14:00:00.558336+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=73843.2
- Funnel: target 773 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +49.44% | $3,774,528.35 |
| PLAY/USDT:USDT | +45.89% | $9,021,215.62 |
| GUN/USDT:USDT | +30.05% | $1,537,813.00 |
| STG/USDT:USDT | +26.52% | $4,825,726.64 |
| TA/USDT:USDT | +21.24% | $2,496,913.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +4.52% | +4.58% |
| MYX/USDT:USDT | below_1h_threshold | +3.82% | +3.89% |
| GUA/USDT:USDT | below_1h_threshold | +2.98% | +3.04% |
| PUNDIX/USDT:USDT | below_1h_threshold | +2.51% | +2.57% |
| UP/USDT:USDT | below_1h_threshold | +1.71% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
