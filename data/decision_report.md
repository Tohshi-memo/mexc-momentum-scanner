# Decision Report

- generated_at: 2026-08-21T17:51:33.965206+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12231, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +1.32% | **+0.49%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.47% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.50% | **+3.50%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.64% | **+1.98%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.59% | **+1.55%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4362件 (Win 1337 / Loss 1434 / Flat 1591) / skip 4430件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.58** / 初期 $100.00 (+56.58%)
- 確定: 1843件 (Win 511 / Loss 437 / Flat 895) / skip 3799件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0568 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T17:51:22.283049+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77408.8
- Funnel: target 1018 → liquid 213 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +25.64% | $11,055,752.07 |
| BEAT/USDT:USDT | +14.27% | $59,086,695.73 |
| BLESS/USDT:USDT | +11.16% | $6,210,319.23 |
| JIMOTHY/USDT:USDT | +7.47% | $1,013,211.66 |
| 1000BONK/USDT:USDT | +7.42% | $14,702,396.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.66% | +4.73% |
| ZORA/USDT:USDT | below_1h_threshold | +4.12% | +4.19% |
| PEPE/USDT:USDT | below_1h_threshold | +4.04% | +4.11% |
| GALA/USDT:USDT | below_1h_threshold | +4.01% | +4.08% |
| STX/USDT:USDT | below_1h_threshold | +3.69% | +3.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
