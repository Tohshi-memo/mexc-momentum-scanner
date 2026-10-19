# Decision Report

- generated_at: 2026-10-19T04:46:40.607088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16984**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16984, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.50% | **-1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.81% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.34% | **+1.07%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.09% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,281.23** / 初期 $100.00 (+1181.23%)
- 確定: 6429件 (Win 1868 / Loss 2053 / Flat 2508) / skip 7116件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,281.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.26** / 初期 $100.00 (+177.26%)
- 確定: 3749件 (Win 1035 / Loss 881 / Flat 1833) / skip 6646件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0116 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $277.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5148件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T04:46:20.657989+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=82734.4
- Funnel: target 1084 → liquid 145 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.1 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +34.50% | $10,704,911.16 |
| ZEREBRO/USDT:USDT | +26.51% | $1,461,169.86 |
| KORU/USDT:USDT | +16.84% | $49,086,054.99 |
| AGT/USDT:USDT | +14.99% | $7,496,347.53 |
| SNXX/USDT:USDT | +12.70% | $12,090,752.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.45% | +3.16% |
| SAND/USDT:USDT | below_1h_threshold | +2.78% | +2.49% |
| KORU/USDT:USDT | below_1h_threshold | +1.78% | +1.50% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.51% | +1.22% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.34% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
