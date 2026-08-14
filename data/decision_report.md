# Decision Report

- generated_at: 2026-08-14T22:46:33.403252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11613**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11613, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.05% | **+0.92%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.58% | **+0.79%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.47% | **+0.45%** |
| LIMIT_5PCT | 2/20 | 10.0% | +4.48% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.97% | **+0.74%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.92% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.05** / 初期 $100.00 (+544.05%)
- 確定: 4081件 (Win 1280 / Loss 1342 / Flat 1459) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $644.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.62** / 初期 $100.00 (+53.62%)
- 確定: 1676件 (Win 481 / Loss 404 / Flat 791) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $153.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 1561件 (Win 476 / Loss 597 / Flat 488) / pending 3件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000322 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-08-14T22:46:19.128194+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62868.3
- Funnel: target 985 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +27.94% | $72,347,529.53 |
| US/USDT:USDT | +23.72% | $6,862,920.29 |
| DOLO/USDT:USDT | +14.78% | $1,628,127.49 |
| GUN/USDT:USDT | +11.44% | $1,010,077.79 |
| ACU/USDT:USDT | +11.24% | $1,902,673.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACU/USDT:USDT | below_1h_threshold | +2.48% | +2.52% |
| BTW/USDT:USDT | below_1h_threshold | +1.97% | +2.01% |
| JTO/USDT:USDT | below_1h_threshold | +1.60% | +1.65% |
| SNXX/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| CAP/USDT:USDT | below_1h_threshold | +1.37% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
