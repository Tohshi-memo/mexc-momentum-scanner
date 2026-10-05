# Decision Report

- generated_at: 2026-10-05T17:26:29.286755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16167**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16167, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.24% | **+0.20%** |
| LIMIT_BB3S | 3/13 | 23.1% | +0.83% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.33% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.19% | **+0.99%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.14% | **+0.98%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.26% | **+0.63%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,305.64** / 初期 $100.00 (+1205.64%)
- 確定: 6226件 (Win 1824 / Loss 1988 / Flat 2414) / skip 6502件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,305.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3610件 (Win 1005 / Loss 845 / Flat 1760) / skip 5968件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0458 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4329件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-05T17:26:14.720934+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=85297.8
- Funnel: target 1074 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +10.17% | $12,777,996.31 |
| BATON/USDT:USDT | +8.08% | $12,619,042.63 |
| US/USDT:USDT | +6.95% | $1,056,880.61 |
| AIN/USDT:USDT | +4.49% | $1,263,871.89 |
| STX/USDT:USDT | +4.23% | $4,278,170.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANA/USDT:USDT | below_1h_threshold | +3.15% | +3.11% |
| RAY/USDT:USDT | below_1h_threshold | +2.00% | +1.95% |
| RLC/USDT:USDT | below_1h_threshold | +1.94% | +1.89% |
| USELESS/USDT:USDT | below_1h_threshold | +1.36% | +1.31% |
| AIN/USDT:USDT | below_1h_threshold | +1.33% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
